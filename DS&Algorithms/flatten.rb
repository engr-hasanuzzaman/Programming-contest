def flatten arr
    ans = []
    arr.each do |elm|
      if elm.is_a?(Array)
        ans += flatten(elm)
      else
        ans << elm
      end
    end
    ans
end
  
  
  RSpec.describe "#flatten" do
    it "should return array with proper flatten output" do
      expect(flatten([1,[2,[3,[4]]]])).to eq([1,2,3,4])
      expect(flatten([1,2,3,4,5])).to eq([1,2,3,4,5])
      expect(flatten([1,[2,[3,4,5]]])).to eq([1,2,3,4,5])
      expect(flatten([1])).to eq([1])
      expect(flatten([])).to eq([])
    end
  end