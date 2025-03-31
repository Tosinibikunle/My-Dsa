/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
    let n1="",n2=""

    for(;!([0,undefined].includes(l1?.next)) || !([0,undefined].includes(l2?.next));) {
        n1+=(l1?.val??0)
        n2+=(l2?.val??0)
        l1=l1?.next
        l2=l2?.next
    }

    let value = (+n1[0] + +n2[0])
    let l3 = new ListNode(value%10, null)
    let l4=l3,b=parseInt(value/10)

    for(let i=1;i<n1.length;i+=1) {
        if(b) {
            value=(+n1[i] + +n2[i] + b)
        } else {
            value=(+n1[i] + +n2[i])
        }
        l4.next=new ListNode(value%10, null)
        b=parseInt(value/10)
        l4=l4?.next
    }
    if(b) l4.next=new ListNode(b, null)
    
    return l3
};