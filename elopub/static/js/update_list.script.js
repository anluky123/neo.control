let list_friends = $(`#list_friends`);
let search_field = document.querySelector('.input-search')
search_field.oninput = function () {
    $.ajax({
        url: '/user_list/',
        type: 'GET',
        data: {'username': search_field.value},
        beforeSend: function() {
            list_friends.empty();
        },
        success: (response) => {
            list_friends.append(response);
        }
    })
};


function invite_friend(id) {
    $.ajax({
        url: '/invite_friend/',
        type: 'GET',
        data: {'inviter_id': id},
        success: (response) => {
            let elem = document.getElementById(id)
            elem.classList.replace('fa-user-plus', 'fa-user-check')
    }
    })
}

function delete_friend(id) {
    $.ajax({
        url: '/delete_friend/',
        type: 'GET',
        data: {'friend': id},
        success: (response) => {
            let elem = document.getElementById('delete_'+id)
            // this is second elem from dropdown menu
            let elemDrop = document.getElementById('delete_drop_'+id)

            elem.remove();
            elemDrop.remove();
    }
    })
}
