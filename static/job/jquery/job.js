$(document).ready(function(){

  $(".table_selected").show()
  $(".table_not_selected").hide()


  // $("#id_OT lable").append("<img class='icon img-circle' src='{% static 'image/icon-1.jpeg' %}'>")
  $("#id_OT lable").html("jazz")

  console.log('hi')
  $("li .label").append("hi")

  $(".OT input ").change(function() {
      $(".OT label").removeClass("case");

      $(this).parent().addClass("case")
  });

  $(".Overtime_pay input ").change(function() {
      $(".Overtime_pay label").removeClass("case");

      $(this).parent().addClass("case")
  });


// .Overtime_pay input
  });
