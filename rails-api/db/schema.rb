
ActiveRecord::Schema[8.1].define(version: 2026_01_04_142720) do
  enable_extension "pg_catalog.plpgsql"

  create_table "shops", force: :cascade do |t|
    t.string "access_scopes", default: "", null: false
    t.datetime "created_at", null: false
    t.datetime "expires_at"
    t.string "refresh_token"
    t.datetime "refresh_token_expires_at"
    t.string "shopify_domain", null: false
    t.string "shopify_token", null: false
    t.datetime "updated_at", null: false
    t.index ["shopify_domain"], name: "index_shops_on_shopify_domain", unique: true
  end
end
