window.addEventListener("load", () => {
  const form = document.getElementById("login");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    let email = document.querySelector("input[name=email]").value;
    let password = document.querySelector("input[name=password]").value;
    let username = document.querySelector("input[name=username]").value;
    let newUser = document.querySelector("input[name=newUser]");
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

    if (newUser.checked) {
      // TODO: CHANGE HOST
      fetch("http://localhost/user", {
        method: "POST",
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
    }

    setTimeout(console.log("Logging in..."), 1500);
    //  TODO: CHANGE HOST
    fetch("http://localhost/login", {
      method: "POST",
      headers: headers,
      body: data,
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        if (data.access_token) {
          //   console.log(data.access_token);
          localStorage.setItem("token", data.access_token);
          window.location.href = "index.html";
        } else {
          window.alert("Invalid Login");
        }
      });
  });
});
