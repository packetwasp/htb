class Article < ApplicationRecord
  belongs_to :user
  validates :user_id, presence: true
  validates :text, presence: true, length: { minimum: 5, maximum: 1024 }
  validates :title, presence: true, length: { minimum: 5, maximum: 30 }
end
