fn dfs(nowh: usize, noww: usize, v: &mut Vec<Vec<char>>) {
    if v[nowh][noww] == 'x' {
        return;
    }
 
    v[nowh][noww] = 'x';
    for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)].iter() {
        let newh = nowh as i32 + dh;
        let neww = noww as i32 + dw;
        if newh >= 0 && newh < 10 && neww >= 0 && neww < 10 {
            dfs(newh as usize, neww as usize, v);
        }
    }
}

use proconio::input;
use proconio::{min,max};
fn main() {
    input!{
        h:usize,
        w:usize,
    }
    let mut ans =10**10;
    ans=min(ans,h*w-3*(h/3)*w);
    ans=min(ans,h*w-3*(w/3)*h);
    ans=min(ans,h*w-3*(w/3)*h);
}