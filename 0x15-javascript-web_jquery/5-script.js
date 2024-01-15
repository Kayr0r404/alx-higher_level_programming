$('document').ready(function(){
    $('DIV#add_item').click(function(){
        $('UL.my_list').add('<li>Item</li>').appendTo( 'UL.my_list' )
    });
});