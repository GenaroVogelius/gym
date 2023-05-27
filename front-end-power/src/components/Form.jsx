import { csrftoken } from "./CSRFToken";



function Form({ setUserData, setNotFound }) {

  const URL = "https://power-gym.onrender.com/"
  
  function handleSubmit(event){
    event.preventDefault()
    // ? como le pusiste un name al input asi lo podes llamar despues del .target
    let input = event.target.input_dni;
    let inputValue = event.target.input_dni.value
    const getUserState = async () => {
      try {
        const response = await fetch(
          `${URL}usuario/${inputValue}`
        );
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


    fetch(`${URL}usuario/${inputValue}`, {
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