const app = {
  'properties': {
    'option_list': {}
  },

  getOptions: () => {
    $.ajax({
      url : './get_options',
      type : 'GET',
      dataType:'json',
      success : function(data) {
          app.properties.option_list = data;
          Object.keys(data).forEach((item) => {
            app.getSelectOptions('#select-' + item, item)
          })
      },
      error : function(request,error)
      {
          alert("Request: "+JSON.stringify(request));
      }
    });
  },

  getSelectOptions: (selectId, select) => {
    $.ajax({
      url : './get_select_options',
      type : 'GET',
      data : {
          'select' : select
      },
      dataType:'json',
      success : function(data) {
          $(selectId).html(data)
          $('#select-' + select).html(data);
      },
      error : function(request,error)
      {
          alert("Request: "+JSON.stringify(request));
      }
    });
  },

  getHowMuchData: () => {
    let res = {};
    Object.keys(app.properties.option_list).forEach((opt) => {
      res[opt] = $('#select-' + opt).val();
    })
    return res;
  },

  howMuch: () => {
    $.ajax({
      url : './get_how_much',
      type : 'GET',
      data : app.getHowMuchData(),
      dataType:'json',
      success : function(data) {
          $('#how_much_answer').text(data['how_much'])
      },
      error : function(request,error)
      {
          alert("Request: "+JSON.stringify(request));
      }
    });
  }
}