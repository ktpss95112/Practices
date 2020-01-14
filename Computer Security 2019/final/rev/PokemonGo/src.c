Entering main.init.
Leaving main.init.

{Entering main.main at /home/terrynini38514/Desktop/PokemonV2.go:38:6.
.0:
    t0 = new string (input)
    t1 = new [1]interface{} (varargs)
    t2 = &t1[0:int]
    t3 = make interface{} <- *string (t0)
    *t2 = t3
    t4 = slice t1[:]
    t5 = fmt.Scanf("%s":string, t4...)
        Entering fmt.Scanf at /usr/lib/go-1.10/src/fmt/scan.go:80:6.
        Leaving fmt.Scanf, resuming main.main at /home/terrynini38514/Desktop/PokemonV2.go:40:14.
    t6 = *t0
    t7 = PikaCheck(t6)

    {Entering main.PikaCheck at /home/terrynini38514/Desktop/PokemonV2.go:6:6.

        arr = local [20]int (a)
        cnt = 0
        while( cnt < len(input) ){
            arr[cnt] = (uint8) input[ cnt ] + (uint8) input[ (cnt + 1) % len(input) ]
            // t10 = cnt + 1:int
            // t92 = phi [0: 0:int, 1: t10]
            cnt += 1;
        }
        // t11 = &arr[0]
        // t12 = arr[0]
        // t13 = arr[0] - 185
        t14 = 0 + arr[0] - 185
        // t15 = &arr[1]
        // t16 = *t15
        t17 = arr[1] - 212
        t18 = t14 + t17
        // t19 = &arr[2]
        // t20 = *t19
        t21 = arr[2] - 172
        t22 = t18 + t21
        // t23 = &arr[3]
        // t24 = *t23
        t25 = arr[3] - 145
        t26 = t22 + t25
        // t27 = &arr[4]
        // t28 = *t27
        t29 = arr[4] - 185
        t30 = t26 + t29
        // t31 = &arr[5]
        // t32 = *t31
        t33 = arr[5] - 212
        t34 = t30 + t33
        // t35 = &arr[6]
        // t36 = *t35
        t37 = arr[6] - 172
        t38 = t34 + t37
        // t39 = &arr[7]
        // t40 = *t39
        t41 = arr[7] - 177
        t42 = t38 + t41
        // t43 = &arr[8]
        // t44 = *t43
        t45 = arr[8] - 217
        t46 = t42 + t45
        // t47 = &arr[9]
        // t48 = *t47
        t49 = arr[9] - 212
        t50 = t46 + t49
        // t51 = &arr[10]
        // t52 = *t51
        t53 = arr[10] - 204
        t54 = t50 + t53
        // t55 = &arr[11]
        // t56 = *t55
        t57 = arr[11] - 177
        t58 = t54 + t57
        // t59 = &arr[12]
        // t60 = *t59
        t61 = arr[12] - 185
        t62 = t58 + t61
        // t63 = &arr[13]
        // t64 = *t63
        t65 = arr[13] - 212
        t66 = t62 + t65
        // t67 = &arr[14]
        // t68 = *t67
        t69 = arr[14] - 204
        t70 = t66 + t69
        // t71 = &arr[15]
        // t72 = *t71
        t73 = arr[15] - 209
        t74 = t70 + t73
        // t75 = &arr[16]
        // t76 = *t75
        t77 = arr[16] - 161
        t78 = t74 + t77
        // t79 = &arr[17]
        // t80 = *t79
        t81 = arr[17] - 124
        t82 = t78 + t81
        // t83 = &arr[18]
        // t84 = *t83
        t85 = arr[18] - 172
        t86 = t82 + t85
        // t87 = &arr[19]
        // t88 = *t87
        t89 = arr[19] - 177
        t90 = t86 + t89
        t91 = t90 == 0
        if t91 goto 4
        return false:bool
    Leaving main.PikaCheck, resuming main.main at /home/terrynini38514/Desktop/PokemonV2.go:41:17.}

    if t7 goto 1 else 3
.3:
    t23 = new [1]interface{} (varargs)
    t24 = &t23[0:int]
    t25 = make interface{} <- string ("Nothing here my d...":string)
    *t24 = t25
    t26 = slice t23[:]
    t27 = fmt.Println(t26...)
        Entering fmt.Println at /usr/lib/go-1.10/src/fmt/print.go:263:6.
        Leaving fmt.Println, resuming main.main at /home/terrynini38514/Desktop/PokemonV2.go:46:20.
    jump 2
.2:
    return
Leaving main.main.}
