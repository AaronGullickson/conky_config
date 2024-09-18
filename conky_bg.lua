--==============================================================================
--                                 conky_bg.lua
--==============================================================================

require 'cairo'

-------------------------------------------------------------------------------
--
-- Rounded Bakground
--

corner_r=45

-- Set the colour and transparency (alpha) of your background.

bg_colour=0x000000

bg_alpha=0.5


function rgb_to_r_g_b(colour,alpha)
        return ((colour / 0x10000) % 0x100) / 255., ((colour / 0x100) % 0x100) / 255., (colour % 0x100) / 255., alpha
end

-------------------------------------------------------------------------------
--
-- Main
--
function conky_main()
    if conky_window == nil then
        return
    end

    local cs = cairo_xlib_surface_create(conky_window.display, conky_window.drawable, conky_window.visual, conky_window.width, conky_window.height)
    local display = cairo_create(cs)

    local updates = conky_parse('${updates}')
    update_num = tonumber(updates)

    cairo_surface_destroy(cs)
    cairo_destroy(display)
end

-------------------------------------------------------------------------------
--
-- Background
--
function conky_background()
    if conky_window == nil then
        return
    end

    local cs = cairo_xlib_surface_create(conky_window.display, conky_window.drawable, conky_window.visual, conky_window.width, conky_window.height)
    local display = cairo_create(cs)

          local w=conky_window.width
          local h=conky_window.height

          cairo_move_to(display,corner_r,0)
          cairo_line_to(display,w-corner_r,0)
          cairo_curve_to(display,w,0,w,0,w,corner_r)
          cairo_line_to(display,w,h-corner_r)
          cairo_curve_to(display,w,h,w,h,w-corner_r,h)
          cairo_line_to(display,corner_r,h)
          cairo_curve_to(display,0,h,0,h,0,h-corner_r)
          cairo_line_to(display,0,corner_r)
          cairo_curve_to(display,0,0,0,0,corner_r,0)
          cairo_close_path(display)

          cairo_set_source_rgba(display,rgb_to_r_g_b(bg_colour,bg_alpha))
          cairo_fill(display)

    cairo_surface_destroy(cs)
    cairo_destroy(display)
end

