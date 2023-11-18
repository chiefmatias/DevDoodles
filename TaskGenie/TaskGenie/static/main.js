$(document).ready(function() {
    $('#add-task-btn').click(function() {
      $('#new-task-form').toggle();
    });
  });

  function toggleTaskCompleted(checkbox) {
    var taskItem = checkbox.closest('.list-group-item');
    var taskId = taskItem.querySelector('.form-check-input').getAttribute('id').replace('checkbox-', '');
    var completed = Boolean($(checkbox).is(":checked"));

    if (completed) {
      taskItem.classList.add('completed');
    } else {
      taskItem.classList.remove('completed');
    }
    $.ajax({
      url: "/task_status",
      type: "POST",
      data: { id: taskId, completed: completed },
      headers: {
        "X-CSRF-Token": $('input[name="csrf_token"]').val()
      },
    });


  }
  $(document).ready(function() {
    $('.form-check-input').on('change', function() {
      toggleTaskCompleted(this);
    });
  });


  $(document).ready(function() {
    $('.btn_edit').on('click', function() {
      const taskId = $(this).data('task-id');
      const taskForm = $(`#edit-task-form-${taskId}`);
      const taskDisplay = $(this).closest('.list-group-item');

      taskDisplay.attr('style', 'display: none !important;');
      taskForm.show();
    });
  });

