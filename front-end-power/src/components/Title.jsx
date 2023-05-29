
import { useState, useEffect } from "react";
function Title(props) {

    const [titleData, SetTitleData] = useState(props.data)

    useEffect(() => {
        SetTitleData(props.data)
        
    }, [props.data])


  if (titleData.sexo === "Masculino") {
    return (
      <>
        <h1> 🕺💪Bienvenido {titleData.nombre} 💪🕺</h1>
      </>
    );
  } else {
    return (
      <>
        <h1>💃💅 Bienvenida {titleData.nombre} 💅💃</h1>;
      </>
    );
  }
}



export default Title