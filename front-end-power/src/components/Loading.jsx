import LoadingEffect  from "./LoadingEffect";

function Loading() {
    return (
      <div
        className="position-fixed  start-50 translate-middle"
        style={{ zIndex: 5, top: "10%" }}
      >
        <div className="d-flex flex-column align-items-center">
          <LoadingEffect></LoadingEffect>

        </div>
      </div>
    );
}

export default Loading;
