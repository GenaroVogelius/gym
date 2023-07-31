

import { useState, useEffect } from "react";
function Subtitle( props ) {
    const [subtitleInfo, setSubtitleInfo] = useState(props.data);
    console.log(subtitleInfo)
    
    useEffect(() => {
    setSubtitleInfo(props.data);
    }, [props.data]);


    if (!subtitleInfo.activo) {
      const vencimiento = new Date(subtitleInfo.vencimiento).toLocaleDateString(
        "en-GB"
      );
      return (
        <>
          <h2>Tu cuota venció el {vencimiento}</h2>
        </>
      );
    } else if (subtitleInfo.daysDiff === 1) {
      return (
        <>
          <h2>Tu cuota vence mañana</h2>;
        </>
      );
    }

      else if (subtitleInfo.daysDiff === 0) {
      return (
        <>
          <h2>Tu cuota vence hoy</h2>;
        </>
      );
  }
  else{
      return (
        <>
          <h2>Tu cuota vence en {subtitleInfo.daysDiff} días</h2>;
        </>
      );
    }
    


}


export default Subtitle