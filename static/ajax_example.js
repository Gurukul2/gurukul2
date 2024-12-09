$(document).ready(function() {
            $('#greeting-form').on('submit', function(event) {
                event.preventDefault(); // Prevent the form from submitting via the browser
                name = $("#name").val();
                $.ajax({
                    type: 'GET',
                    url: '/greet',
                    data: {'name': name},
                    success: function(response) {
                        $('#response').html('<p>' + response.greeting + '</p>');
                    },
                    error: function(xhr) {
                        $('#response').html('<p>An error occurred: ' + xhr.responseJSON.greeting + '</p>');
                    }
                });
            });
        });


$(document).ready(function(){
    $("#submit").on('click', function(){
        const selectedId = $("#value").val();
        $.ajax({
            type:'GET',
            url: '/filtered_data',
            data: {"id": selectedId},
            success: function(response){
            const tbody = $("#table-tbody");
            tbody.empty(); //Clear the content of table not header
            if (response.length === 0){
                tbody.append(`<tr><td colspan="5">No Data available for ${selectedId}</tr></td>`);
            }
            else{
            response.forEach(row => {
                 tbody.append(`
                 <tr>
                 <td>${row.ID}</td>
                 <td>${row.Name}</td>
                 <td>${row.Age}</td>
                 <td>${row.Department}</td>
                 <td>${row.Salary}</td>
                 </tr>
                 `);
            });
            }
            },
            error: function(){
            alert("An error has occured")
            }
        })
    })
})