function eGet(getUrl, cbOk, cbErr) {
    $.ajax({ url: getUrl, type: 'GET', success: cbOk, error: cbErr });
}

function activate(menuId, itemId) {
    // inactivate all, then activate the Chosen One
    $('#' + menuId).children().each(function(i) {
        $(this).attr('class', 'nav-inactive');
    });
    if (itemId !== undefined) {
        $('#' + itemId).attr('class', 'nav-active');
    }
}

function buildOnClick(f, p1, p2, p3) {
    // build an onclick attribute, something like this (with the quotes):
    // onclick="menu1('config')"
    s = 'onclick="' + f + '(';
    if (p1 !== undefined) {
        s += "'" + p1 + "'";
        if (p2 !== undefined) {
            s += ", '" + p2 + "'";
            if (p3 !== undefined) {
                s += ", '" + p3 + "'";
            }
        }
    }
    s += ')"';
    return s;
}

$(document).ready(function(){
    // build top row of buttons (config | status | command)
    eGet('http://localhost:5000/api',
        // on success
        function(data, textStatus, jqXHR) {
            $('#menu1').empty();
            for (i in data) {
                id = data[i];
                attr = ' id="' + id + '"';
                attr += ' ' + buildOnClick('menu1', id);
                $('#menu1').append('<button' + attr + '>' + id + '</button>');
            }
            activate('menu1');
        },
        // on error
        function(jqXHR, textStatus, errorThrown) {
            $('#menu1').empty();
        });
});

function menu1(topLevel) {
    // a button in the div 'menu1' was clicked
    // topLevel is the button: 'config', 'status', or 'command'
    console.log('menu1(' + topLevel + ')');
    // make one of the menu1 buttons look active, others inactive
    activate('menu1', topLevel);
    // build second row of buttons (system | acme)
    eGet('http://localhost:5000/api/' + topLevel,
        function(data) {
            $('#data').empty();
            $('#menu3').empty();
            $('#menu2').empty();
            for (i in data) {
                group = data[i];
                attr = ' id="' + group + '"';
                attr += buildOnClick('menu2', topLevel, group);
                $('#menu2').append('<button' + attr + '>' + group + '</button>');
            }
            // make all menu2 buttons look inactive
            activate('menu2');
        },
        function(jqXHR) {
            $('#data').empty();
            $('#menu3').empty();
            $('#menu2').empty();
        });
}

function menu2(topLevel, group) {
    // a button in the div 'menu2' was clicked
    // topLevel is the active menu1 button: 'config', 'status', 'command'
    // group is the menu2 button clicked: 'system', 'acme'
    console.log('menu2(' + topLevel + ', ' + group + ')');
    activate('menu2', group);
    // read group sections and build third row of buttons
    eGet('http://localhost:5000/api/' + topLevel + '/' + group,
        function(data) {
            $('#data').empty();
            $('#menu3').empty();
            for (i in data) {
                section = data[i];
                attr = ' id="' + section + '"';
                attr += buildOnClick('menu3', topLevel, group, section);
                $('#menu3').append('<button' + attr + '>' + section + '</button>');
            }
            // make all menu3 buttons look inactive
            activate('menu3');
        },
        function(jqXHR) {
            $('#data').empty();
            $('#menu3').empty();
        });
}

function menu3(topLevel, group, section) {
    // a button in the div 'menu3' was clicked
    // topLevel is the active menu1 button: 'config', 'status', 'command'
    // group is the active menu2 button: 'system', 'acme'
    // section is the menu3 button clicked: <section name>
    console.log('menu3(' + topLevel + ', ' + group + ', ' + section + ')');
    activate('menu3', section);
    // read section and display
    eGet('http://localhost:5000/api/' + topLevel + '/' + group + '/' + section,
        function(data) {
            // build table of config items in 'data' table
            $('#data').empty();
            for (key in data) {
                value = data[key];
                $('#data').append('<tr>' +
                                  '<td>' + key + '</td>' +
                                  '<td>:</td>' +
                                  '<td style="text-align:right">' + value + '</td>' +
                                  '</tr>');
            }
        },
        function(jqXHR) {
            $('#data').empty();
        });
}
