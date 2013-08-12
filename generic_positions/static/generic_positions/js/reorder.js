$(document).ready(function() {
    // Admin or frontend?
    if ($('#result_list').length > 0) {
        // Set this to the name of the column holding the position
        pos_field = 'position';

        // Determine the column number of the position field
        pos_col = null;

        cols = $('#result_list tbody tr:first').children();
        for (i = 0; i < cols.length; i++) {
            inputs = $(cols[i]).find('input[name*=' + pos_field + ']');

            if (inputs.length > 0) {
                // Found!
                pos_col = i;
                break;
            }
        }

        if (pos_col == null) {
            return;
        }

        // Some visual enhancements
        var header = $('#result_list thead tr').children()[pos_col];
        $(header).css('width', '1em');
        $(header).children('a').text('#');
        $(header).find('.sortremove').remove();

        // Hide position field
        $('#result_list tbody tr').each(function(index) {
            pos_td = $(this).children()[pos_col];
            input = $(pos_td).children('input').first();
            //input.attr('type', 'hidden')
            input.hide();

            label = $('<strong>' + input.attr('value') + '</strong>');
            $(pos_td).append(label);
        });

        // Determine sorted column and order
        sorted = $('#result_list thead th.sorted');
        sorted_col = $('#result_list thead th').index(sorted);
        sort_order = sorted.hasClass('descending') ? 'desc' : 'asc';

        if (sorted_col != pos_col) {
            // Sorted column is not position column, bail out
            console.info("Sorted column is not %s, bailing out", pos_field);
            return;
        }

        $('#result_list tbody tr').css('cursor', 'move');

        // Make tbody > tr sortable
        $('#result_list tbody').sortable({
            axis: 'y',
            items: 'tr',
            cursor: 'move',
            update: function(event, ui) {
                item = ui.item;
                items = $(this).find('tr').get();

                if (sort_order == 'desc') {
                    // Reverse order
                    items.reverse();
                }

                $(items).each(function(index) {
                    pos_td = $(this).children()[pos_col];
                    input = $(pos_td).children('input').first();
                    label = $(pos_td).children('strong').first();

                    input.attr('value', index);
                    label.text(index);
                });

                // Update row classes
                $(this).find('tr').removeClass('row1').removeClass('row2');
                $(this).find('tr:even').addClass('row1');
                $(this).find('tr:odd').addClass('row2');

                // Submit form and save positions
                $.post($('#position_update_url').val(), $('#changelist-form').serializeArray());
            }
        });

        // Order rows by position
        $(header).click(function(){
            if ($(header).hasClass('ascending')) {
                $(header).removeClass('ascending').addClass('descending');
                $(header).find('a').removeClass('ascending').addClass('descending');
                var inverse = false;
            } else if ($(header).hasClass('descending')) {
                $(header).removeClass('descending').addClass('ascending');
                $(header).find('a').removeClass('descending').addClass('ascending');
                var inverse = true;
            }

            var th = $(this),
                thIndex = th.index(),
                table = $('#result_list');
            table.find('td').filter(function(){
                return $(this).index() === thIndex;
            }).sortElements(function(a, b){
                if( parseInt($.text([a])) == parseInt($.text([b])) )
                    return 0;
                return parseInt($.text([a])) > parseInt($.text([b])) ?
                    inverse ? -1 : 1
                    : inverse ? 1 : -1;
            }, function(){
                // parentNode is the element we want to move
                return this.parentNode;
            });
            inverse = !inverse;

            // Update row classes
            $('#result_list tbody').find('tr').removeClass('row1').removeClass('row2');
            $('#result_list tbody').find('tr:even').addClass('row1');
            $('#result_list tbody').find('tr:odd').addClass('row2');
            return false;
        }).click(); // Initial sorting.
    } else {
        $('#positionContainer').children().css('cursor', 'move');
        $('#positionContainer').sortable({
            update: function(event, ui) {
                items = $(this).children().each(function(index) {
                    $(this).find('.positionInput').attr('value', index);
                    $(this).find('.positionVisible').text(index);
                });

                // Submit form and save positions
                $form = $(this).closest('form');
                $.post(
                    $form.attr('action')
                    ,$form.serializeArray()
                );
            }
        });

    }
});


// Sorting function
jQuery.fn.sortElements = (function(){
    var sort = [].sort;
    return function(comparator, getSortable) {
        getSortable = getSortable || function(){return this;};
        var placements = this.map(function(){
            var sortElement = getSortable.call(this),
                parentNode = sortElement.parentNode,
                // Since the element itself will change position, we have
                // to have some way of storing it's original position in
                // the DOM. The easiest way is to have a 'flag' node:
                nextSibling = parentNode.insertBefore(
                    document.createTextNode(''),
                    sortElement.nextSibling
                );
            return function() {
                if (parentNode === this) {
                    throw new Error(
                        "You can't sort elements if any one is a descendant of another."
                    );
                }
                // Insert before flag:
                parentNode.insertBefore(this, nextSibling);
                // Remove flag:
                parentNode.removeChild(nextSibling);
            };
        });
        return sort.call(this, comparator).each(function(i){
            placements[i].call(getSortable.call(this));
        });
    };
})();