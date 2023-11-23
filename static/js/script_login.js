const togglePassword = document.querySelector("#togglePassword");

const password = document.querySelector("#id_password");

togglePassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);

    // toggle the icon    
    var textContent = togglePassword.innerText || togglePassword.textContent;
    togglePassword.innerHTML = textContent;
    if (textContent == "visibility_off") {
        document.querySelector('#togglePassword').textContent = "visibility";
    }
    else {
        document.querySelector('#togglePassword').textContent = "visibility_off";
    }    
});


function login_error(type_error) {
    if (type_error == 'user_not_cpf') {
        return Swal.fire({
            icon: 'warning',
            title: 'USUÁRIO INCORRETO!',
            text: 'O usuário informado não é somente números. Preencha o USUÁRIO (CPF) corretamente!',
        });
    }
    else if (type_error == 'not_active') {
        return Swal.fire({
            icon: 'info',
            title: 'USUÁRIO INATIVO!',
            text: 'Seu Usuário foi Inativado. Por favor, consulte o Administrador/Gestor do Sistema!',
        });
    } 
    else {
        return Swal.fire({
            icon: 'error',
            title: 'USUÁRIO E/OU SENHA INVÁLIDO!',
            text: 'Preencha o USUÁRIO (CPF) e SENHA corretamente',
        });
    }
}