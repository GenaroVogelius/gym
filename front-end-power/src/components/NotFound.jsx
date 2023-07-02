import Spans from "./Asthetics/Spans";

function NotFound() {
  return (
    <div className="login-box">
      <Spans></Spans>
      <h1>🤔 El DNI ingresado no se encuentra en la base de datos 🤔</h1>
    </div>
  );
}

export default NotFound;
