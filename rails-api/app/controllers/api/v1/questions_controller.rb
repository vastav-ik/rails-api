module Api
  module V1
    class QuestionsController < ApplicationController

      def create
        store_id = params[:store_id]
        question = params[:question]

        if store_id.blank? || question.blank?
          render json: { error: "Missing store_id or question" }, status: :unprocessable_entity
          return
        end

        service = AiAgentService.new(store_id)
        result = service.ask(question)

        render json: result
      end
    end
  end
end
