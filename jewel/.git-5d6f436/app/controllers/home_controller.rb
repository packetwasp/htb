class HomeController < ApplicationController
  def index
    @article = Article.order("created_at").last
  end
end
