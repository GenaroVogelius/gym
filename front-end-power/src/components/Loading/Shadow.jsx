const Shadow = ({ children }) => (
  <div
    className="shadow"
    style={{
      opacity: 0.5,
      width: "100vw",
      height: "100vh",
      backgroundColor: "rgba(0, 0, 0, 0%)",
    }}
  >
    {children}
  </div>
);

export default Shadow
