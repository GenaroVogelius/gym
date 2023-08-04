import { csrftoken } from "./Utils/CSRFToken";



function Form({ setUserData, setNotFound, setIsLoading }) {
  const URL = "https://vps-3503468-x.dattaweb.com/";
  // const URL = "https://power-gym.com.ar/";

  // URL FOR DEVELOP
  // const URL = "http://localhost:8000/"
  // const URL = import.meta.env.VITE_URL;
  
  // console.log(URL);

  // // "https://vps-3503468-x.dattaweb.com/";

  function handleSubmit(event) {
    setIsLoading(true);
    event.preventDefault();
    // ? como le pusiste un name al input asi lo podes llamar despues del .target
    let input = event.target.input_dni;
    let inputValue = event.target.input_dni.value;
    const getUserState = async () => {
      try {
        const response = await fetch(`${URL}usuario/${inputValue}`);
        const data = await response.json();
        setIsLoading(false);

        if ("not found" in data) {
          setNotFound(true);
        } else {
          setUserData(data);
          // inputValue = "" no te funciona por eso hiciste la variable input
        }
        input.value = "";
      } catch (error) {
        console.log("Error:", error.message);
      }
    };
    getUserState();

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
      <div className="user-box">
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