document.addEventListener("keydown", function (event) {
  if (event.altKey) {
    document.getElementById("searh_modal_popup").click();
  }
});

console.log("Hello World");

//! Hide the product popup
document.getElementById("close_product_popup").onclick = function() {
    document.getElementById("product_popup").style.display = "none";
    document.getElementById("product_popup").style.visibility = "hidden";
  };