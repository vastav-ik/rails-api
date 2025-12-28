
require 'faraday'

class AiAgentService
  AI_SERVICE_URL = ENV.fetch('AI_SERVICE_URL', 'http://localhost:8000')

  def initialize(store_id)
    @store_id = store_id
  end

  def ask(question)
    response = conn.post('/api/v1/analyze') do |req|
      req.headers['Content-Type'] = 'application/json'
      req.body = {
        store_id: @store_id,
        question: question
      }.to_json
    end

    if response.success?
      JSON.parse(response.body)
    else
      { error: "AI Service Error: #{response.status}" }
    end
  rescue Faraday::Error => e
    { error: "AI Connection Failed: #{e.message}" }
  end

  private

  def conn
    @conn ||= Faraday.new(url: AI_SERVICE_URL)
  end
end
