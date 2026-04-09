import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Para medir el rendimiento de la app, puedes pasar una función
// para registrar resultados (por ejemplo: reportWebVitals(console.log))
// o enviarlos a un endpoint de analítica. Más información: https://bit.ly/CRA-vitals
reportWebVitals();
