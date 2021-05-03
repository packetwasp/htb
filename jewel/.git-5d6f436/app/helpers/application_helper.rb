module ApplicationHelper
  def gravatar_for(user, options = { size: 80})
    gravatar_id = Digest::MD5::hexdigest(user.email.downcase)
    size = options[:size]
    gravatar_url = "https://secure.gravatar.com/avatar/#{gravatar_id}?s=#{size}&d=identicon"
    image_tag(gravatar_url, alt: user.username, class: "img-circle")
  end

#  def will_paginate(collection_or_options = nil, options = {})
#    if collection_or_options.is_a? Hash
#      options, collection_or_options = collection_or_options, nil
#    end
#    unless options[:renderer]
#      options = options.merge renderer: WillPaginate::ActionView::BootstrapLinkRenderer
#    end
#    super *[collection_or_options, options].compact
#  end
end
