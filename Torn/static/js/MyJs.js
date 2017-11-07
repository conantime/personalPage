  $(document).ready(function () {
       $("#file").change(function () {
           var file =  $("#file")[0].files[0];
           var form = new FormData();
           form.append("k1","v1");
           form.append("fi",file);
            $.ajax({
                type:'POST',
                url: '/personal_info',
                data: form,
                processData: false,  // tell jQuery not to process the data
                contentType: false,  // tell jQuery not to set contentType
                before :function(xmlHttp){
                xmlHttp.setRequestHeader("If-Modified-Since","0");
                xmlHttp.setRequestHeader("Cache-Control","no-cache");
                },
                success: function(arg){
                    window.location.href="/"
                }
           })
       })
   });