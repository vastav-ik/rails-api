
import requests

class ShopifyClient:
    def __init__(self, shop_url: str, access_token: str):
        self.shop_url = shop_url
        self.access_token = access_token
        self.api_version = "2024-01"

    def execute_gql(self, query: str):
        url = f"https://{self.shop_url}/admin/api/{self.api_version}/graphql.json"
        headers = {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        }
        
        if self.access_token == "mock_token":
            return {"data": {"mock": "result"}}

        try:
            response = requests.post(url, json={"query": query}, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def execute_shopify_ql(self, query: str):
        gql_wrapper = f"""
        {{
            shopifyqlQuery(query: "{query}") {{
                __typename
                ... on TableResponse {{
                    tableData {{
                        rowData
                        columns {{
                            name
                            dataType
                        }}
                    }}
                }}
                ... on ParseErrors {{
                    message
                }}
            }}
        }}
        """
        return self.execute_gql(gql_wrapper)
