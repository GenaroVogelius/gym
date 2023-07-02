import LoadingLetters from "./LoadingLetters";

function LoadingBox() {
  return (
    <div
      className="position-fixed  start-50 translate-middle"
      style={{ zIndex: 5, top: "10%" }}
    >
      <div className="d-flex flex-column align-items-center">
        <LoadingLetters></LoadingLetters>
      </div>
    </div>
  );
}

export default LoadingBox;
