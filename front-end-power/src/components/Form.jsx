import { csrftoken } from "./CSRFToken";



function Form({ setUserData, setNotFound }) {
  
  function handleSubmit(event){
    event.preventDefault()
    // ? como le pusiste un name al input asi lo podes llamar despues del .target
    let input = event.target.input_dni;
    let inputValue = event.target.input_dni.value
    const getUserState = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/usuario/${inputValue}`);
        const data = await response.json();
        
        if ("not found" in data) {
          setNotFound(true);
          input.value = "";
        } else {
          setUserData(data);
          // inputValue = "" no te funciona
          input.value = "";
        }
      } catch (error) {
        console.log("Error:", error.message);
      }
    }
    getUserState()


    fetch(`http://127.0.0.1:8000/usuario/${inputValue}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    });
  }


    return (
      <form onSubmit={handleSubmit}>
        <div class="user-box">
          <label>Ingrese su D.N.I</label>
          <input
            className="input"
            type="text"
            required
            name="input_dni"
            autoFocus
            autoComplete="off"
          />
        
        </div>
      </form>
    );

}

export default Form;