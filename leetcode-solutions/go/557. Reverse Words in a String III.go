// https://leetcode.com/problems/reverse-words-in-a-string-iii/

import "strings"

func revStr(s string) string {
    sA := strings.Split(s, "")
    for i, j := 0, len(sA)-1; i < j; i, j = i+1, j-1 {
        sA[i], sA[j] = sA[j], sA[i]
    }
    
    return strings.Join(sA, "")
}
func reverseWords(s string) string {
    aW := strings.FieldsFunc(s, func(r rune) bool {
        return r == ' '
    })
    
    for i, s := range aW {
        aW[i] = revStr(s)
    }
    
    return strings.Join(aW, " ")
}