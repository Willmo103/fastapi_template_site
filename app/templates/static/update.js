window.addEventListener("load", () => {
  const form = document.getElementById("update");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    let email = document.querySelector("input[name=email]").value;
    let password = document.querySelector("input[name=password]").value;
    let username = document.querySelector("input[name=username]").value;
    let data = JSON.stringify({
      email: email,
      password: password,
      username: username,
    });
    // console.log(data);
    const headers = {
      "Content-Type": "application/json",
      "Access-Control-Origin": "*",
    };
    // TODO: CHANGE HOST
    fetch("http://localhost/user", {
      method: "PUT",
      headers: headers,
      body: data,
    })
      .then(function (response) {
        if (response.ok) {
          return response.json();
        } else {
          window.alert("Email already in use!");
          return;
        }
      })
      .then(function (data) {
        if (data) {
          console.log("New User Created\n", data);
          window.alert("New User Saved! Logging in...");
        }
      });
  });
});
