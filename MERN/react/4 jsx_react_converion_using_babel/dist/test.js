"use strict";

function Myh1Component() {
  return /*#__PURE__*/React.createElement("h1", null, "Hello React");
}
var root = document.getElementById("root");
var div_container = ReactDOM.createRoot(root);
div_container.render( /*#__PURE__*/React.createElement(Myh1Component, null));