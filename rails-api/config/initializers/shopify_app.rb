
ShopifyApp.configure do |config|
  config.application_name = "AI Analytics"
  config.api_key = ENV['SHOPIFY_API_KEY']
  config.secret = ENV['SHOPIFY_API_SECRET']
  config.old_secret = ""
  config.scope = ENV.fetch('SCOPES', 'read_products,read_orders,read_inventory')
  config.embedded_app = true
  config.after_authenticate_job = false
  config.api_version = "2024-01"
  config.shop_session_repository = 'ShopifyApp::InMemorySessionStore'
  config.log_level = :info
  config.reauth_on_access_scope_changes = true
  
end
