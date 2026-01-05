import React, { useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

function App() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [currentView, setCurrentView] = useState(null);

  const handleAsk = async () => {
    if (!question) return;
    setLoading(true);

    try {
      const response = await axios.post(
        "http://localhost:3000/api/v1/questions",
        {
          store_id: "ai-analytics-3.myshopify.com",
          question: question,
        }
      );

      const newEntry = {
        question: question,
        answer: response.data.answer,
        intent: response.data.intent,
        chartData: response.data.chart_data || [],
        timestamp: new Date().toLocaleTimeString(),
      };

      setHistory([newEntry, ...history]);
      setCurrentView(newEntry);
      setQuestion("");
    } catch (err) {
      alert("Connection failed. Ensure services are running.");
    }
    setLoading(false);
  };

  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        backgroundColor: "#f6f6f7",
        fontFamily: "sans-serif",
      }}
    >
      <div
        style={{
          width: "250px",
          backgroundColor: "#fff",
          borderRight: "1px solid #d2d5d9",
          padding: "20px",
          overflowY: "auto",
        }}
      >
        <h3 style={{ color: "#008060", fontSize: "16px" }}>Recent Questions</h3>
        {history.map((item, index) => (
          <div
            key={index}
            onClick={() => setCurrentView(item)}
            style={{
              padding: "10px",
              marginBottom: "10px",
              borderRadius: "4px",
              cursor: "pointer",
              fontSize: "13px",
              backgroundColor: currentView === item ? "#f1f8f5" : "transparent",
              border:
                currentView === item
                  ? "1px solid #008060"
                  : "1px solid transparent",
            }}
          >
            <strong>{item.timestamp}</strong>: {item.question.substring(0, 30)}
            ...
          </div>
        ))}
      </div>

      <div style={{ flex: 1, padding: "50px" }}>
        <div
          style={{
            maxWidth: "800px",
            margin: "0 auto",
            background: "white",
            padding: "30px",
            borderRadius: "12px",
            boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
          }}
        >
          <h2 style={{ color: "#008060", textAlign: "center" }}>
            Shopify AI Analytics
          </h2>

          <div style={{ display: "flex", gap: "10px", marginBottom: "30px" }}>
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask about sales, inventory, or customers..."
              style={{
                flex: 1,
                padding: "12px",
                borderRadius: "6px",
                border: "1px solid #babfc3",
              }}
            />
            <button
              onClick={handleAsk}
              disabled={loading}
              style={{
                padding: "12px 24px",
                backgroundColor: "#008060",
                color: "white",
                border: "none",
                borderRadius: "6px",
                cursor: "pointer",
                fontWeight: "bold",
              }}
            >
              {loading ? "Thinking..." : "Ask AI"}
            </button>
          </div>

          {currentView && (
            <div>
              <div
                style={{
                  padding: "15px",
                  borderLeft: "4px solid #008060",
                  backgroundColor: "#f1f8f5",
                  marginBottom: "20px",
                }}
              >
                <strong>{currentView.question}</strong>
                <p
                  style={{
                    lineHeight: "1.5",
                    whiteSpace: "pre-wrap",
                    marginTop: "10px",
                  }}
                >
                  {currentView.answer}
                </p>
              </div>

              {currentView.chartData.length > 0 && (
                <div style={{ height: "300px", width: "100%" }}>
                  <h4 style={{ textAlign: "center", color: "#6d7175" }}>
                    Trend Analysis ({currentView.intent})
                  </h4>
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={currentView.chartData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="name" />
                      <YAxis />
                      <Tooltip />
                      <Bar
                        dataKey="value"
                        fill="#008060"
                        radius={[4, 4, 0, 0]}
                      />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
