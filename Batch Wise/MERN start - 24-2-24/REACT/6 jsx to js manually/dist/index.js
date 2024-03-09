"use strict";

function MyComponent() {
  return /*#__PURE__*/React.createElement("h1", null, "This h1 is created in JSX");
}
var root = document.getElementById("root");
var reactRoot = ReactDOM.createRoot(root);
reactRoot.render( /*#__PURE__*/React.createElement(MyComponent, null));