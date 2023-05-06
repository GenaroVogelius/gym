import { useState, useEffect } from 'react'
import './style/css/style.css'
import Form from "./components/Form";


function App() {
  const [userData, setUserData] = useState(null);
  const [background, setBackground] = useState("");
  const [showWelcome, setShowWelcome] = useState(false);
  const [notFound, setNotFound] = useState(false);

  
  
  useEffect(() => {
    if (userData && userData.activo) {
      setBackground("linear-gradient(rgb(47 167 4), rgb(96 235 5))");
      setShowWelcome(true);
    } else if (userData && !userData.activo) {
      setBackground("linear-gradient(rgb(155 3 3), rgb(240 7 7))");
      setShowWelcome(true);
    }

    if (notFound) {
      setBackground("linear-gradient(rgb(200 189 5), rgb(240 225 7))");
    }

      const timer = setTimeout(() => {
        setBackground("linear-gradient(#f0f0f0, #d4d4d4)");
        setShowWelcome(false);
        setNotFound(false);
        setUserData(null);
      }, 4000);
    
    
    return () => clearTimeout(timer);
  }
  // ? cleanup function in useEffect is used to clear the timer when the component unmounts or updates.
    
  , [userData, notFound]);

  useEffect(() => {
    document.body.style.background = background;
  }, [background]);


  // ? en react si pones autofocus es Focus con la f en mayuscula a diferencia de html


  if (showWelcome) {
    const today = new Date();
    const vencimiento = userData.vencimiento;
    const timeDiff = new Date (vencimiento) - today;
    const daysDiff = (Math.ceil(timeDiff / (1000 * 3600 * 24))) + 1;
    // tuviste que ponerle +1 porque sino no te daba
  
    
    function Title() {

      function Subtitle() {
        if (!userData.activo) {
          
          const vencimiento = new Date(userData.vencimiento).toLocaleDateString(
            "en-GB"
          );
          return (
            <>
              <h2>
                Tu cuota venció el {vencimiento}
              </h2>
            </>
          )
        }

        else {
          return (
            <>
              <h2>Tu cuota vence en {daysDiff} días</h2>;
            </>)
        }
      
      }

      if (userData.sexo === "Masculino") {
        return (
          <>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <h1> 🕺💪Bienvenido {userData.nombre} 💪🕺</h1>
            <Subtitle />
          </>
        );
      } else {
        return (
          <>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <h1>💃💅 Bienvenida {userData.nombre} 💅💃</h1>;
            <Subtitle />
          </>
        );
      }
    }
        return (
          <div className="login-box">
            <Title />
          </div>
        )
  }
  
  else if (notFound) {

    function Title() {
        return (
          <h1>🤔 El DNI ingresado no se encuentra en la base de datos 🤔</h1>
        );
    }
    
    return (
      <div className="login-box">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <Title />
      </div>
    );
  }
    
  else {
    return (
      <div className="login-box">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <h1>Bienvenido/a al Power Gym</h1>
        <Form {...{ setUserData, setNotFound }} />
      </div>
    );
  }
}

export default App
