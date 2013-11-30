function login(user, pass, callback) {
        $.post("login", {
                username : user,
                password : pass
        }, function(d) {
                if (d.indexOf("success") > -1) callback(true);
                else callback(false);
        });
}

function register(user, pass, callback) {
        $.post("register", {
                username : user,
                password : pass,
        },function(d) {
                if (d.indexOf("success") > -1) callback(true);
                else callback(false, d);
        });
}

function logout(callback) {
        $.post("logout", {}, function(d) {
                if (d.indexOf("success") > -1) callback(true);
                else callback(false);
        });
}
