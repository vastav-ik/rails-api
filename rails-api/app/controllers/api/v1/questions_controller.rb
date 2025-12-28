
module Api
  module V1
    class QuestionsController < ApplicationController
      # In a real app, we would authenticate using ShopifyApp::Authenticated
      # include ShopifyApp::Authenticated

      # Skip CSRF for API
      skip_before_action :verify_authenticity_token

      def create
        store_id = params[:store_id]
        question = params[:question]

        if store_id.blank? || question.blank?
          render json: { error: "Missing store_id or question" }, status: :unprocessable_entity
          return
        end

        # Call AI Service
        service = AiAgentService.new(store_id)
        result = service.ask(question)

        render json: result
      end
    end
  end
end
