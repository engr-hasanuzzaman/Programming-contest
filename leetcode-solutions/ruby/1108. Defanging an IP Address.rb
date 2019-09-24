# https://leetcode.com/problems/defanging-an-ip-address/

# @param {String} address
# @return {String}
def defang_i_paddr(address)
  address.gsub(".", "[.]")
end