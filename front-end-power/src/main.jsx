import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './style/css/style.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <div className="background">
      <App />
    </div>
  </React.StrictMode>,
)
