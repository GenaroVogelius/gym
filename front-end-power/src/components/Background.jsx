import { useState, useEffect } from "react";


function Background() {

    const [backgroundType, setBackgroundType] = useState("");

    return (
        <div className={`background${backgroundType}`}>
            <App { ...setBackgroundType } />
        </div>
  );
}

export default Background;
