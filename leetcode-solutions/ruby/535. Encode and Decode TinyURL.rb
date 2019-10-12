# https://leetcode.com/problems/encode-and-decode-tinyurl/

@stol = {}
@ltos = {}
VALID_CHAR = (0..9).to_a + ('a'..'z').to_a + ('A'..'Z').to_a
# Encodes a URL to a shortened URL.
#
# @param {string} longUrl
# @return {string}
def encode(longUrl)
    return @ltos[longUrl] if @ltos[longUrl]
    ran = random
    
    while @stol[ran]
        ran = random
    end
    srt_url = "http://tinyurl.com/#{ran}"
    @ltos[longUrl] = srt_url
    @stol[srt_url] = longUrl
    srt_url
end

# Decodes a shortened URL to its original URL.
#
# @param {string} shortUrl
# @return {string}
def decode(shortUrl)
    @stol[shortUrl]
end

def random(len=6)
    VALID_CHAR.sample(len)
end
# Your functions will be called as such:
# decode(encode(url))