import "strings"

func reverseWords(s string) string {
    ans := strings.FieldsFunc(s, func(r rune) bool {
        return r == ' '
    })
    

    //fmt.Println(ans, len(ans))
    for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
        ans[i], ans[j] = strings.Trim(ans[j], " "), strings.Trim(ans[i], " ")
    }
    return strings.Join(ans, " ")   
}