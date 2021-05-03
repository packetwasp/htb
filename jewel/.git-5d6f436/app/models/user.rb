class User < ActiveRecord::Base
 has_many :articles
 has_secure_password
 VALID_USER_REGEX = /\A[\w\d]+\z/
 VALID_EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
 validates :username, presence: true, uniqueness: { case_sensitive: false }, length: { minimum: 3, maximum: 25 },
                      format: { with: VALID_USER_REGEX }
 validates :email, presence: true, length: { maximum: 105 }, uniqueness: { case_sensitive: false }, 
                   format: { with: VALID_EMAIL_REGEX }
 before_save { self.email = email.downcase }
end
