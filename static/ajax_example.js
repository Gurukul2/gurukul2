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