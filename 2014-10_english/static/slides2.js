
$(document).ready(function() {

    /* If not doing a live presentation, keep slide stack vertical. */

    var end_param = $.url.param('end');
    if (!end_param)
        return;

    /* Only style the deck once. */

    if (typeof already !== 'undefined')
        return;
    already = true;

    /* Presentation style. (Op, op, op, op!) */

    $('body').removeClass('reading-mode').addClass('presentation-mode');

    /* Live presentations get identically-sized scrolling slides. */

    var slide_width = 1024;
    var slide_height = 768;
    var slide_gap = 200;    // px between outgoing and incoming big slide
    var slide_margin = 20;  // px between big slide and thumbnails
    var slide_scale = 0.2;
    var duration = window.slide_transition_time ||
        500;                // animated motion duration, in ms

    $('.section').wrap('<div class="slide" />');

    /* Global state */

    $slides = $('.slide');
    current_slide_n = -1;
    last_slide_change = null;

    /* Functions */

    var minus = function(boolValue) { return boolValue ? '-' : ''; }

    var select_slide = function(n) {
        window.location = '#' + n + '';
    }

    var select_slide_based_on_hash = function() {
        var n = location.hash ? parseInt(location.hash.substring(1)) : 0;
        if (current_slide_n != -1)
            $slides.eq(current_slide_n).removeClass('current-slide');
        current_slide_n = n;
        $slides.eq(current_slide_n).addClass('current-slide');

        /* Remember when the slide was last changed. */
        last_slide_change = new Date();

        /* Update the status line immediately. */
        timer_update();
    }

    var thumbpos = function(n) {
        var slot = n - current_slide_n;
        var left = slot * slide_width * slide_scale;
        return {left: left + 'px',
                top: (0.6 * slide_height + slide_margin) + 'px'};
    }

    /* Event bindings */

    window.onhashchange = select_slide_based_on_hash;

    var leftKeys = [33, 37, 38, 66];
    var rightKeys = [32, 34, 39, 40, 70];

    $('html').bind('keydown', function(event) {
        if (rightKeys.indexOf(event.keyCode) !== -1) {
            event.preventDefault();
            if (current_slide_n < $slides.length - 1)
                select_slide(current_slide_n + 1);
        } else if (leftKeys.indexOf(event.keyCode) != -1) {
            event.preventDefault();
            if (current_slide_n > 0)
                select_slide(current_slide_n - 1);
        }
    });

    /* Timer */

    var timer_update = function() {
        timer_div.removeClass('emergency');

        var now = new Date();
        if (!endtime) {
            readout = 'Time ' + now.toTimeString().substring(0, 5) +
                '<br>' + current_slide_n + '/' + ($slides.length - 1);
        } else {
            var left = Math.floor((endtime - now) / 1000);
            var leftm = Math.floor(left / 60);
            var lefts = left % 60;
            readout = ('' + current_slide_n + '/' + ($slides.length - 1) +
                       '<br>' + leftm + 'm' + lefts + 's');
            if (last_slide_change) {
                var til_end = endtime - last_slide_change;
                var slides_left = $slides.length - current_slide_n;
                var time_per_slide = til_end / slides_left;
                var ss = (last_slide_change - now) + time_per_slide;
                readout += ('<br>' + Math.floor(ss / 1000) + 's');
                if (ss < 0)
                    timer_div.addClass('emergency');
            }
        }
        timer_div.html(readout);
    }

    var timer_div = $('<div class="timer"></div>');
    $('body').append(timer_div);

    var endtime = null;
    if (end_param) {
        hours = parseInt(end_param.substring(0, end_param.length - 2));
        minutes = parseInt(end_param.substring(end_param.length - 2));
        var endtime = new Date();
        if (hours || hours === 0)
            endtime.setHours(hours);
        endtime.setMinutes(minutes);
        endtime.setSeconds(0);
        endtime.setMilliseconds(0);
    }

    /* Kick things off. */

    select_slide_based_on_hash();
    setInterval(timer_update, 1000);
});
