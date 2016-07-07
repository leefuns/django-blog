KindEditor.options.filterMode = false;

KindEditor.ready(function(K) {
                window.editor = K.create('#id_content',{
                	width:'800px',
                	height:'300px',
                	uploadJson:'/admin/upload/KindEditor',
                });
        });