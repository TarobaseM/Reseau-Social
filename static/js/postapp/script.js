$(document).ready(function() {
    // Lorsque le bouton est cliqué
    $('.likes-count').click(function() {
        var $likesList = $(this).next('.likes-list');
        // Vérifier si l'élément est visible
        if ($likesList.is(':visible')) {
            // S'il est visible, le cacher
            $likesList.hide();
        } else {
            // S'il est est caché, le montrer
            $likesList.show();
        }
    });
    $('.commenter').click(function(event) {
        event.stopPropagation();
        
        var $commentList = $(this).prev('.comform');
        // Vérifier si l'élément est visible
        if ($commentList.is(':visible')) {
            // S'il est visible, le cacher
            $commentList.hide();
        } else {
            // S'il est est caché, le montrer
            $commentList.show();
        }
    });
    
});
