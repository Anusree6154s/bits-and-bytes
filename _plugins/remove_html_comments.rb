module Jekyll
  module RemoveHtmlComments
    def remove_html_comments(input)
      input.gsub(/<!--.*?-->/m, '')
    end
  end
end

Liquid::Template.register_filter(Jekyll::RemoveHtmlComments)