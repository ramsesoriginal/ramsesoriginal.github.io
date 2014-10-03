# An example Jekyll Liquid tag. Utilizes the new plugin system.
#
# 1. Make a _plugins directory in your jekyll site, and put this class in a file there.
# 2. In anyone of your pages, you can use the 'render_time' liquid tag like so:
#     {% render_time Page generated at: %}
 
module Jekyll
  class RenderTimeTag < Liquid::Tag
 
    def initialize(tag_name, text, tokens)
      super
      @text = text
    end
 
    def render(context)
    	Time.now.strftime(context.registers[:site].config['date_format'] + " " + context.registers[:site].config['time_format'])
    end
  end
end
 
Liquid::Template.register_tag('render_time', Jekyll::RenderTimeTag)